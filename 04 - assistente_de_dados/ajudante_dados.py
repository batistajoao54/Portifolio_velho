import os
import time
import tkinter as tk  # Somente para a janela
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Função para exibir uma notificação do sistema
def exibir_notificacao(titulo, mensagem):
    if os.name == 'nt':  # Verifica se o sistema operacional é Windows
        from plyer import notification
        notification.notify(
            title=titulo,
            message=mensagem,
            app_name='Seu Aplicativo'
        )
    elif os.name == 'posix':  # Verifica se o sistema operacional é baseado em POSIX (Linux ou macOS)
        os.system(f'notify-send "{titulo}" "{mensagem}"')

# Função para registrar a alteração e exibir notificação
def registrar_alteracao(arquivo, mensagem):
    with open(arquivo_de_log, 'a', encoding='utf-8') as log:
        log.write(mensagem + '\n')
    exibir_notificacao('Alteração de Arquivo/Pasta', mensagem)

# Obtenha o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Crie um diretório para armazenar o arquivo de log
pasta_log = os.path.join(diretorio_atual, 'log')
os.makedirs(pasta_log, exist_ok=True)

# Nome do arquivo de log
arquivo_de_log = os.path.join(pasta_log, 'log_de_alteracoes.txt')

# Dicionário para rastrear o estado anterior dos arquivos e pastas
estado_anterior = {}

# Classe que lida com eventos de alteração em arquivos e pastas
class MeuManipuladorDeEventos(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            arquivo = event.src_path
            tamanho = os.path.getsize(arquivo)
            data_modificacao = time.ctime(os.path.getmtime(arquivo))
            data_criacao = time.ctime(os.path.getctime(arquivo))

            # Verifique se o evento ocorre dentro da pasta 'log' e, se for o caso, ignore-o
            if pasta_log in arquivo:
                return

            # Verifique se o arquivo foi modificado desde o último registro
            if arquivo not in estado_anterior or estado_anterior[arquivo] != (tamanho, data_modificacao):
                # Atualize o estado anterior do arquivo
                estado_anterior[arquivo] = (tamanho, data_modificacao)

                # Crie a mensagem da alteração
                mensagem = f'Arquivo modificado: {arquivo}\nTamanho: {tamanho} bytes\nData de modificação: {data_modificacao}\nData de criação: {data_criacao}'

                # Registre a alteração e exiba a notificação
                registrar_alteracao(arquivo_de_log, mensagem)

    def on_created(self, event):
        if event.is_directory:
            nova_pasta = event.src_path

            # Crie a mensagem da criação de pasta
            mensagem = f'Nova pasta criada: {nova_pasta}'

            # Registre a criação de pasta e exiba a notificação
            registrar_alteracao(arquivo_de_log, mensagem)

        else:
            novo_arquivo = event.src_path

            # Crie a mensagem da criação de arquivo
            mensagem = f'Novo arquivo criado: {novo_arquivo}'

            # Registre a criação de arquivo e exiba a notificação
            registrar_alteracao(arquivo_de_log, mensagem)

    def on_deleted(self, event):
        if event.is_directory:
            pasta_deletada = event.src_path

            # Crie a mensagem da exclusão de pasta
            mensagem = f'Pasta deletada: {pasta_deletada}'

            # Registre a exclusão de pasta e exiba a notificação
            registrar_alteracao(arquivo_de_log, mensagem)

        else:
            arquivo_deletado = event.src_path

            # Crie a mensagem da exclusão de arquivo
            mensagem = f'Arquivo deletado: {arquivo_deletado}'

            # Registre a exclusão de arquivo e exiba a notificação
            registrar_alteracao(arquivo_de_log, mensagem)

    def on_moved(self, event):
        origem = event.src_path
        destino = event.dest_path

        # Crie a mensagem da movimentação de arquivo ou pasta
        mensagem = f'Arquivo ou pasta movido de: {origem} para {destino}'

        # Registre a movimentação e exiba a notificação
        registrar_alteracao(arquivo_de_log, mensagem)

# Crie um observador para monitorar o diretório atual
observer = Observer()
observer.schedule(MeuManipuladorDeEventos(), diretorio_atual, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
