import zipfile
import os.path
import shutil

#file1 = os.path.join("excel", "decembre.xlsx")
#file2 = os.path.join("excel", "novembre.xlsx")
#file3 = os.path.join("excel", "octobre.xlsx")
'''
fichier_zip = zipfile.ZipFile("fichiers_excel.zip","w",zipfile.ZIP_DEFLATED)        # zipfile.ZIPL_DEFLATED pas obligatoire mais ca permet de compresser le fichier
fichier_zip.write("excel/decembre.xlsx")                                            # pour qu'il prenne moins de place
fichier_zip.write("excel/novembre.xlsx")
fichier_zip.write("excel/octobre.xlsx")
fichier_zip.close()
'''
# shutil.make_archive("fichiers_excel2", "zip", "excel")

shutil.unpack_archive("fichiers_excel2.zip", "extraction_zip")