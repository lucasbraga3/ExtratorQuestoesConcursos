import re
import pypdf
import glob

pdf_collection = glob.glob("*.pdf")
i = 1
f = open('output.txt', 'w')
for pdf in pdf_collection:
    leitor = pypdf.PdfReader(pdf)
    questoes = []

    for page in leitor.pages:
        corpo = page.extract_text()
        finder = re.compile(
    r"Questão (\d+)\s*\n+" 
        r"([\s\S]+?)\n+"  
        r"\(A\) (.*?)\n+" 
        r"\(B\) (.*?)\n+"  
        r"\(C\) (.*?)\n+"  
        r"\(D\) (.*?)(?=\nQuestão|\Z)",re.MULTILINE)
        resultado = finder.findall(corpo)
        questoes.append(resultado)
    f.write("_"*25 + "prova " + str(i) + "_"*25)
    f.write('\n')
    for questao in questoes:
        if(len(questao) != 0):
            for quest in questao:
                numero, enunciado, a, b, c, d = quest
                f.write(f"Questão {numero}:\n{enunciado.strip()}")  
                f.write('\n')
                f.write(f"A) {a.strip()}")
                f.write('\n')
                f.write(f"B) {b.strip()}")
                f.write('\n')
                f.write(f"C) {c.strip()}")
                f.write('\n')
                f.write(f"D) {d.strip()}")
                f.write('\n')
                f.write("-" * 50)
                f.write('\n')
    f.write("_"*25 + "prova " + str(i) + "_"*25)
    f.write('\n')
    i = i + 1
