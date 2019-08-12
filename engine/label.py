startLabel = r"\{\{start[\s]+([\S]+)[\s]*\}\}\n"
endLabel = r"\{\{end[\s]+([\S]+)[\s]*\}\}"
scopeLabel = startLabel + r"(.*?)[\s]+" + endLabel

getterLabel = r"\{\{=[\s]*(.*?)[\s]*\}\}"
setterLabel = r"\{\{([^=].*?)[\s]*\}\}"
