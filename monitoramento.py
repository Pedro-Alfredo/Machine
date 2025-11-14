import psutil

class Monitoramento:
    def listar(self):
        processos = []
        for p in psutil.process_iter(["pid", "name"]):
            processos.append(p.info)
        return processos
