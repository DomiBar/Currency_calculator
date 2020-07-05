from flask import Flask, render_template, request, redirect()
import main

app=Flask(__name__)

@app.route('/calculator', methods=['GET','POST'])
def calculator():
    pass