from PIL import Image, ImageOps, ImageDraw, ImageFont
import json,os
SRC='/private/tmp/claude-501/-Users-ludvigthunberg-Claude---All-Brands/6077966b-9d20-4494-9f38-56b501b49f70/scratchpad/vind'
OUT=os.path.expanduser('~/Vindhora/vind')
os.makedirs(OUT,exist_ok=True)
BOX=json.load(open('/tmp/vh/boxes.json'))
cache={}
def im(f):
    if f not in cache: cache[f]=ImageOps.exif_transpose(Image.open(f'{SRC}/{f}.jpg'))
    return cache[f]
made=[]
for k,(f,x0,y0,x1,y1) in BOX.items():
    src=im(f); W,H=src.size
    c=src.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
    c.thumbnail((640,640),Image.LANCZOS)
    c.save(f'{OUT}/{k}.jpg',quality=86)
    made.append((k,c))
print(len(made),'utklipp skrivna')
# kontaktkartor, 30 per ark
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',14)
except: font=ImageFont.load_default()
cols,cw,ch=6,220,240
for n in range(0,len(made),30):
    part=made[n:n+30]
    sheet=Image.new('RGB',(cols*cw,((len(part)+cols-1)//cols)*ch),'white'); d=ImageDraw.Draw(sheet)
    for i,(k,img) in enumerate(part):
        t=img.copy(); t.thumbnail((cw-14,ch-42),Image.LANCZOS)
        x=(i%cols)*cw; y=(i//cols)*ch
        sheet.paste(t,(x+7+(cw-14-t.width)//2,y+28)); d.text((x+6,y+7),k[:26],fill='black',font=font)
    sheet.save(f'/tmp/vh/sheet_{n//30}.jpg',quality=86)
print('kontaktkartor:',(len(made)+29)//30)
