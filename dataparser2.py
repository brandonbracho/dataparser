Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pdfplumber


def parse_data(file):
    all_tables=[]
    with pdfplumber.open(file) as pdf:
        page=pdf.pages
        for page in pdf.pages:
            text=page.extract_text()
            all_tables.append(page.extract_tables())
    i=0
    while i<5:
        for table in all_tables:
            for t in table:
                for b in t:
                    for c in b:
                        if c==""or c==None:
                            b.remove(c)
        i+=1
                            
                        
    machine_names=[]
    data=[]
    totals=[]
    for table in all_tables:
        for t in table:
            machine_names.append(t[0])
            data+=[l[0::3] for l in t[2:-1]]
            totals+=[t[-1][0::3]]
            
    return machine_names, data, totals 
