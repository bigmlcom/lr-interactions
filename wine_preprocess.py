from csv import DictReader, DictWriter

def process_row(r,t):
    #ks = list(r.keys())
    #ks.remove('quality')
    #for k in ks:
    #    interaction_key = k + ' * type'
    #    r[interaction_key] = float(r[k])*t
    r['type'] = t
    r['good wine'] = int(r['quality']) > 5
    return r

with open('winequality-white.csv') as fid:
    reader =  DictReader(fid, delimiter = ';')
    white_rows = [process_row(r,0) for r in reader]
    
with open('winequality-red.csv') as fid:
    reader =  DictReader(fid, delimiter = ';')
    red_rows = [process_row(r,1) for r in reader]
                 
all_rows = white_rows + red_rows

with open('winequality-all.csv','w') as fid:
    ks = list(all_rows[0].keys())
    ks.remove('type')
    ks = ['type'] + ks
    writer = DictWriter(fid,fieldnames=ks)
    writer.writeheader()
    writer.writerows(all_rows)