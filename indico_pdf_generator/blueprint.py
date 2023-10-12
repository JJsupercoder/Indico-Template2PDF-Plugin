from flask import Blueprint, render_template, request

from indico.web.util import jsonify_template

from flask import Flask, render_template, Response
import json
from xhtml2pdf import pisa  # pip install xhtml2pdf
from io import BytesIO


blueprint = Blueprint("indico_pdf_generator", __name__, template_folder="templates")


@blueprint.route("/template1")
def template1():
    data = read_json()
    return render_template(
        "indico_pdf_generator/template1.html",
        title=data["title"],
        heading=data["heading"],
        content=data["content"],
    )


@blueprint.route("/template2")
def template2():
    data = read_json()
    return render_template(
        "indico_pdf_generator/template2.html",
        title=data["title"],
        heading=data["heading"],
        content=data["content"],
    )


def read_json(
    json_file="indico-pdf-generator/indico_pdf_generator/data.json",
):
    file = open(json_file)  # Opening JSON file
    data = json.load(file)  # returns JSON object as a dictionary
    file.close()  # Closing file
    return data


@blueprint.route("/template1/generate_pdf")
def generate_pdf_template1():
    data = read_json()
    rendered_html = render_template(
        "indico_pdf_generator/template1.html",
        title=data["title"],
        heading=data["heading"],
        content=data["content"],
    )
    pdf_data = BytesIO()
    pisa.CreatePDF(rendered_html, dest=pdf_data)
    pdf_data.seek(0)

    return Response(pdf_data, content_type="application/pdf")


@blueprint.route("/template2/generate_pdf")
def generate_pdf_template2():
    data = read_json()
    rendered_html = render_template(
        "indico_pdf_generator/template2.html",
        title=data["title"],
        heading=data["heading"],
        content=data["content"],
    )
    pdf_data = BytesIO()
    pisa.CreatePDF(rendered_html, dest=pdf_data)
    pdf_data.seek(0)

    return Response(pdf_data, content_type="application/pdf")


@blueprint.route("/generate_pdf", methods=["GET", "POST"])
def generate_pdf():
    if request.method == "POST":
        pass
        # data handling part from JSON file

    return render_template("indico_pdf_generator/index.html")
