import argparse
import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

TITLE_FONT_SIZE = 80
TAG_FONT_SIZE = 64
PAD = 24
MAX_TAGS = 4

font_path = './assets/OpenSans-Regular.ttf'
base_img_path = './assets/leetcode_canvas.png'
# title_text = '157/158 Read N Characters Given Read 4 I/II'
# difficultiy_tag = 'Easy'
# topic_tags = 'String|String|String|String'
name_text = 'Ren Zhang'
out_dir = './outputs'
os.makedirs(out_dir,  exist_ok=True)
base = Image.open(base_img_path)

diff_tag_color = {
    'Easy': 'green',
    'Medium': 'yellow',
    'Hard': 'red'
}

def get_word_size(word, font_size):
    big_count = sum(map(lambda x:x.isupper(), word))
    sml_count = len(word) - big_count
    return big_count * font_size + sml_count * font_size // 2

def text_to_multiline(text, font_size, pad, line_width):
    multiline_text = []
    curr_line_width = 2 * pad
    for word in text.split():
        word_size = get_word_size(word, font_size)
        if curr_line_width + word_size > line_width:
            multiline_text.append("\n")
            curr_line_width = 2 * pad
        multiline_text.append(word)
        curr_line_width += word_size
    return " ".join(multiline_text)

def parse_topic_tags(tags, font_size, pad, line_width):
    tags = ' '.join(tags.split('|')[:MAX_TAGS])
    return text_to_multiline(tags, font_size, pad, line_width)

def make_save_filename(title_text):
    title_text = ''.join(c for c in title_text if c.isalnum())
    return title_text + '_thumbnail.png'

def make_thumbnail(title_text, difficultiy_tag, topic_tags):
    multiline_title_text = text_to_multiline(title_text, TITLE_FONT_SIZE, PAD, base.size[0])
    diff_tag_offset = (multiline_title_text.count('\n') +1) * TITLE_FONT_SIZE + PAD * 2
    topic_tag_offset = (multiline_title_text.count('\n') +2) * TITLE_FONT_SIZE + PAD * 3
    name_text_offset_h = base.size[0] - get_word_size(name_text, TAG_FONT_SIZE) + PAD
    name_text_offset_v = base.size[1] - PAD - TAG_FONT_SIZE
    multiline_tags = parse_topic_tags(topic_tags, TAG_FONT_SIZE, PAD, base.size[0])
    image = base.copy()
    title_font = ImageFont.truetype(font_path, TITLE_FONT_SIZE)
    tag_font = ImageFont.truetype(font_path, TAG_FONT_SIZE)
    draw = ImageDraw.Draw(image) 
    draw.multiline_text((PAD, PAD), multiline_title_text, font = title_font, fill='black') 
    draw.text((PAD,diff_tag_offset), difficultiy_tag, font = tag_font, fill=diff_tag_color[difficultiy_tag]) 
    draw.multiline_text((PAD,topic_tag_offset), multiline_tags, font = tag_font, fill='gray') 
    draw.text((name_text_offset_h,name_text_offset_v), name_text, font = tag_font, fill='black') 
    image.save(os.path.join(out_dir, make_save_filename(title_text)))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser('parameters to program')
    parser.add_argument('mode', type=str, default='single', choices=['single', 'batch'])
    parser.add_argument('--title', type=str, default='')
    parser.add_argument('--diff', type=str, default='')
    parser.add_argument('--tags', type=str, default='')
    parser.add_argument('--csv', type=str, default='')
    args = parser.parse_args()
    
    if args.mode == 'single':
        assert all((args.title, args.diff, args.tags)), 'need input for single processing'
        make_thumbnail(args.title, args.diff, args.tags)
    else:
        assert args.csv, 'need csv file for batch processing'
        df = pd.read_csv(args.csv)
        for i, row in tqdm(df.iterrows(), total=df.shape[0]):
            make_thumbnail(row['title'], row['diff'], row['tags'])
