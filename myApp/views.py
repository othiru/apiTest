from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from lxml import etree
import os
from .models import organizationInfo

# Create your views here.
def mainRedirect(request):
    return HttpResponseRedirect("home")


def main(request):
    if request.method == "POST":
        try:
            # Form data collection
            org_Name = request.POST["orgName"]
            org_Email = request.POST["orgEmail"]
            org_Contact = request.POST["orgContact"]
            org_Address = request.POST["orgAddress"]
            admin_Name = request.POST["admName"]
            admin_Desig = request.POST["admDesg"]
            admin_Email = request.POST["admEmail"]
            admin_Contact = request.POST["admMobile"]

            # Form data save into model
            mainInfo = organizationInfo(
                orgName = org_Name,
                orgEmail = org_Email,
                orgContact = org_Contact,
                orgAddress = org_Address,
                adminName = admin_Name,
                adminDesig = admin_Desig,
                adminEmail = admin_Email,
                adminContact = admin_Contact,
                )
            mainInfo.save()

            try:
                # XML data prepare
                data = {
                    "orgName" : org_Name,
                    "orgEmail" : org_Email,
                    "orgContact" : org_Contact,
                    "orgAddress" : org_Address,
                    "adminName" : admin_Name,
                    "adminDesig" : admin_Desig,
                    "adminEmail" : admin_Email,
                    "adminContact" : admin_Contact,
                }

                # XML File create
                xml_data = '<data>'
                for key, value in data.items():
                    xml_data += f'<{key}>{value}</{key}>'
                xml_data += '</data>'

                # XML File save
                media_directory = settings.MEDIA_ROOT
                xmlFileName1 = org_Name + "_1.xml"
                xmlFileName2 = org_Name + "_2.xml"

                # XML File save (without xsl file)
                xml_file_path1 = os.path.join(media_directory, xmlFileName1)
                with open(xml_file_path1, 'w', encoding='utf-8') as file1:
                    file1.write('<?xml version="1.0" encoding="UTF-8"?>')
                    file1.write(xml_data)

                # XML File save (with xsl file)
                xml_file_path2 = os.path.join(media_directory, xmlFileName2)
                with open(xml_file_path2, 'w', encoding='utf-8') as file2:
                    file2.write('<?xml version="1.0" encoding="UTF-8"?>')
                    xslFile = '<?xml-stylesheet type="text/xsl" href="/static/css/xmlShow.xsl"?>'
                    file2.write(xslFile)
                    file2.write(xml_data)

                try:
                    # Load the XML data
                    root = etree.fromstring(xml_data)

                    # Load the XSLT stylesheet
                    xslt_path = os.path.join(settings.BASE_DIR, 'myApp', 'static', 'css', 'xmlShow.xsl')
                    xslt_doc = etree.parse(xslt_path)
                    transform = etree.XSLT(xslt_doc)

                    # Apply the XSLT transformation
                    result_tree = transform(root)

                    # Get the HTML string from the result_tree
                    form_data = str(result_tree)
                    return render(request, "xmlShow.html", {"form_data": form_data})
                except Exception as e:
                    print("Error XML Transformation: ", e)
            except Exception as e:
                print("Error Saving XML Data: ", e)
        except Exception as e:
            print("Error Saving Data in Model: ", e)

    return render(request, "main.html")
