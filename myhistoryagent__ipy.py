# -*- coding: utf-8 -*-
"""Myhistoryagent_.ipy

Original file is located at
    https://colab.research.google.com/drive/1ZZZtsG6zM0qeibY0d9TfRkMvTZ931oLW
"""

!pip install google-generativeai --quiet
!pip install ipywidgets --quiet #tp create a beautiful ui

import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown

API_KEY = "ADD_APIKEY"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

topic_input = widgets.Text(
    description = "Topic",
    layout = widgets.Layout(width = '400px')
)
style_input = widgets.Dropdown(
    description = "style",
    options = ['Timeline', 'Short story',],
    layout = widgets.Layout(width = '400px')
)
audience_input = widgets.Text(
    description = "Audience",
    layout = widgets.Layout(width = '400px')
)
hashtag_input = widgets.Text(
    description = "Hashtags",
    layout = widgets.Layout(width = '400px')
)
submit_button = widgets.Button(
    description = "Generate Tweet",
    button_style = 'primary',
    tooltip = 'click to generate twwet',
    layout = widgets.Layout(width = '400px')
)
output = widgets.Output()

def generate_tweet(b):
  output.clear_output()
  prompt = f"""
  You are a historian .give me a brief history of {topic_input.value}.
  generate a tweet about the topic "{topic_input.value}".
  use a format it will display{style_input.value}.
  generate tweet for audience {audience_input.value}.
  Include the hastages {hashtag_input.value}.
  keep it under 280 characters
  """
  with output:
    try:
      response = model.generate_content(prompt)
      tweet = response.text.strip()
      display(Markdown(f"### Generated Tweet : \n\n {tweet} "))
    except Exception as e:
      print("Error",e)
submit_button.on_click(generate_tweet)

form = widgets.VBox([
    widgets.HTML(value="<h3> 🔎History Generator Agent</h3"),
    topic_input,
    style_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])
display(form)

