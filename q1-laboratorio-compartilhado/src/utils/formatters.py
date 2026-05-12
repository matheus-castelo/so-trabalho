from src.utils.colors import Colors

def extrair_timeline_simples(timeline_rica):
    timeline_formatada = []
    for estado in timeline_rica:
        item = estado["processo"]
        if item == "idle":
            timeline_formatada.append(f"{Colors.RED}{Colors.BOLD}idle{Colors.RESET}")
        else:
            timeline_formatada.append(str(item))
            
    return " -> ".join(timeline_formatada)