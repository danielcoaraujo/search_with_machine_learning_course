from flask import g, current_app
from opensearchpy import OpenSearch

def get_opensearch():
    if 'opensearch' not in g:
        host = 'localhost'
        port = 9200
        auth = ('admin', 'admin')

        client = OpenSearch(
            hosts = [{'host': host, 'port': port}],
            http_compress = True,
            http_auth = auth,
            use_ssl = True,
            verify_certs = False,
            ssl_assert_hostname = False,
            ssl_show_warn = False,
        )
        g.opensearch = client

    return g.opensearch
