import camelot
tables = camelot.read_pdf('pdf.pdf', pages='all')
tables[0].df
tables.export('found_table.csv', f='csv')
tables[0].parsing_report

