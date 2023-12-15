import yaml
from custom import stress, greeting, sad, anxiety_state, happy, anxiety, depression, trauma, addiction, insomnia, \
    narcolepsy, fobias, bulimia

file_path = [ r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\config.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\domain.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\entities.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\intents.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\responses.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\rules.yaml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\stories.yml",
              r"C:\Users\elmer\PycharmProjects\FreudBot\Rasa Project\syn.yaml"]

combined_data = {}


for file_path in file_path:
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        combined_data.update(yaml_data)

        def get_combined_data():
            return combined_data


        intent_logic = {
            'saludar': greeting,
            'estado_animo_triste': sad,
            'estado_animo_ansioso': anxiety_state,
            'estado_animo_feliz': happy,
            'estres': stress,
            'ansiedad': anxiety,
            'depresion': depression,
            'estres_post_traumatico': trauma,
            'adiccion': addiction,
            'insomnio': insomnia,
            'narcolepsia': narcolepsy,
            'Fobias': fobias,
            'Bulimia': bulimia
        }

