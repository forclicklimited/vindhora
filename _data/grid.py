from PIL import Image, ImageOps, ImageDraw, ImageFont
import sys,os
SRC='/private/tmp/claude-501/-Users-ludvigthunberg-Claude---All-Brands/6077966b-9d20-4494-9f38-56b501b49f70/scratchpad/vind'
f=sys.argv[1]
im=ImageOps.exif_transpose(Image.open(f'{SRC}/{f}.jpg')).convert('RGB')
im.thumbnail((1100,1100),Image.LANCZOS); W,H=im.size
d=ImageDraw.Draw(im)
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',20)
except: font=ImageFont.load_default()
for i in range(1,10):
    x=int(W*i/10); y=int(H*i/10)
    d.line([(x,0),(x,H)],fill=(255,0,0),width=1); d.line([(0,y),(W,y)],fill=(255,0,0),width=1)
    d.text((x+3,3),f'{i/10:.1f}',fill=(255,0,0),font=font)
    d.text((3,y+3),f'{i/10:.1f}',fill=(0,120,255),font=font)
im.save(f'/tmp/vh/grid_{f}.jpg',quality=88); print(f'/tmp/vh/grid_{f}.jpg',im.size)
