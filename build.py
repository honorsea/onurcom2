import json
import os

def build_site():
    # Define the languages and their output filenames
    config = {
        'en': 'index.html',
        'fr': 'index_fr.html',
        'tr': 'index_tr.html'
    }

    # Load the master template
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Generate each file
    for lang, output_file in config.items():
        with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
            translations = json.load(f)

        html_content = template
        
        # Replace all {{ key }} placeholders with JSON values
        for key, value in translations.items():
            placeholder = f"{{{{ {key} }}}}"
            html_content = html_content.replace(placeholder, str(value))

        # Write the final HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Success.")

if __name__ == '__main__':
    build_site()