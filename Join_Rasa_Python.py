import yaml


file_path = [ r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\config.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\domain.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\entities.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\intents.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\responses.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\rules.yaml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\stories.yml",
              r"C:\Users\elmer\PycharmProjects\Freud_AI\Rasa Project\syn.yaml"]

combined_data = {}


for file_path in file_path:
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        combined_data.update(yaml_data)

        def get_combined_data():
            return combined_data



