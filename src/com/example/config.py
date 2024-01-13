class Config:
    def __init__(self):
        self.es_scheme = "http"
        self.es_host = "localhost"
        self.es_port = "9200"
        self.es_host_another = "localhost"
        self.es_port_another = "9201"
        self.es_port_transport_another = "9301"
        self.es_url = f"{self.es_scheme}://{self.es_host}:{self.es_port}"
