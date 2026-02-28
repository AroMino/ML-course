import json, base64, os

with open('RAKOTOARIJAONA_Aro_Mino_Avotra.ipynb', 'r') as f:
    nb = json.load(f)

os.makedirs('figures', exist_ok=True)

count = 0
for i, cell in enumerate(nb['cells']):
    for out in cell.get('outputs', []):
        data = out.get('data', {})
        if 'image/png' in data:
            with open(f'figures/fig_cell{i}_{count}.png', 'wb') as img:
                img.write(base64.b64decode(data['image/png']))
            count += 1

print(f"{count} images exportées")
