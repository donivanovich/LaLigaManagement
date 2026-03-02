from repositories.entrenador_repository import EntrenadorRepository

class EntrenadorService:

    @staticmethod
    def get_all():
        return EntrenadorRepository.get_all()

    @staticmethod
    def create(data):
        return EntrenadorRepository.create(data)