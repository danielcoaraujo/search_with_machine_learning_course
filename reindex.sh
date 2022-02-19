#!/bin/sh
reindex_init () {
    echo "Killing previous logstash running instance"
    kill -9 $(pgrep -f 'logstash')

    echo "Removing logstash data files ..."
    rm /workspace/logstash/logstash-7.13.2/products_data/plugins/inputs/file/.sincedb_*

    echo "Removing indices ..."
    sh delete-indexes.sh
    
    echo "Indexing data ..."
    sh index-data.sh
}


reindex_init