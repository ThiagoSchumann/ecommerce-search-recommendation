from src.infra.api_docs.swagger.swagger_adapter import SwaggerAdapter

def configure_dependencies():
    # Configuração das dependências
    api_docs_adapter = SwaggerAdapter()
    return api_docs_adapter
