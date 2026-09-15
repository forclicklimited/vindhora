import json,re,subprocess,sys,urllib.parse
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
def fetch(url):
    r=subprocess.run(['curl','-s','-m','30','-A',UA,'-L',url],capture_output=True)
    return r.stdout.decode('utf-8','replace')
def products(q):
    url='https://lyko.com/sv/sok?q='+urllib.parse.quote(q)
    h=fetch(url)
    m=re.search(r'window\.CURRENT_PAGE\s*=\s*(\{.*?\});\s*\n',h,re.S)
    if not m: return []
    try: d=json.loads(m.group(1))
    except Exception as e: return []
    return d.get('trackingInformationProducts') or []
def img(name,pid):
    slug=re.sub(r'[^a-z0-9.]+','-',name.lower()).strip('-')
    return f"https://lyko.com/globalassets/product-images/{slug}-{pid}_1.jpg"
if __name__=='__main__':
    for q in sys.argv[1:]:
        ps=products(q)
        print(f"--- {q}: {len(ps)} träffar")
        for p in ps[:4]:
            print('   ',p['name'],'|',p['brand'],'|',p['price'],'|',p['id'])
            print('     ',img(p['name'],p['id']))
