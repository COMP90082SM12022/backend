import json

from selenium import webdriver
import threading
import os
import time
from PIL import Image


def shot(dr, imgs):
    """循环截图函数"""
    while True:
        try:
            png_data = dr.get_screenshot_as_png()
            imgs.append(png_data)
            # time.sleep(0.1)
        except Exception:
            break


img_dir = 'img'  # 临时图片目录

options = webdriver.EdgeOptions()
options.add_argument("--headless")

dr = webdriver.Edge(options=options)
dr.set_window_size(800, 800)

imgs = []
t = threading.Thread(target=shot, args=(dr, imgs))

dr.get('http://localhost:3001/test')
t.start()
start_time = time.time()
storage = dr.execute_script('return localStorage.getItem("fileContent");')
storage = json.loads(storage)
steps = len(storage['visualStages'])
print(len(storage['visualStages']))
end_time = time.time()
time.sleep(0.2 * steps + 1 + float(end_time - start_time))
dr.quit()

for index, img in enumerate(imgs):
    with open(os.path.join(img_dir, f'{index}.png'), 'ab') as f:
        f.write(img)

img_list = os.listdir(img_dir)
img_list.sort(key=lambda x: int(x[:-4]))

first_img = Image.open(os.path.join(img_dir, img_list[0]))
else_imgs = [Image.open(os.path.join(img_dir, img)) for img in img_list[1:]]

first_img.save("record.gif", append_images=else_imgs,
               duration=100,
               save_all=True)
