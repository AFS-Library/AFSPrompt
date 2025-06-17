#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: wang
@time: 2025/5/22 16:03
@desc: 
"""
from promptcap import PromptCap

model = PromptCap("models/promptcap-coco-vqa")

def get_img_caption(question, image):
    prompt = f"please describe this image according to the given question: {question}"
    caption = model.caption(prompt, image)
    return caption

