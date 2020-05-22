import csv

csv_input_filename = "message_types.csv"

template = {"page": {}, "category": {}, "message": {}}
template["page"][
    "header"
] = """---
description: >-
  Messages are used to communicate information between Mycroft services and
  other components. This list of Message types outlines the details and provides
  sample code for each.
---

# Message Types

Each Message type listed contains a description outlining it's meaning or purpose. Where relevant, the Message type will also list the specific JSON data packets expected to be emitted with that Message, and the most common producers and consumers of the Message.

See the [MessageBus documentation](message-bus.md) for further information on this service and examples of using Messages.
"""

template["category"][
    "header"
] = """
## {category}
"""

template["message"] = {
    "header": """
### {message_type}

{description}

""",
    "data": """**Data:**

```JSON
{message_data}
```

""",
    "actors": """<table>
  <thead>
    <tr>
      <th style="text-align:left">Producer</th>
      <th style="text-align:left">Consumer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">
        {producer}
      </td>
      <td style="text-align:left">
        {consumer}
      </td>
    </tr>
  </tbody>
</table>

""",
    "usage": """**Usage:**

{{% tabs %}}
{{% tab title="Message handler in MycroftSkill" %}}
```python
...
def initialize(self):
    self.add_event('{message_type}',
                   self.{message_handler_title})

def {message_handler_title}(self, message):
    # code to excecute when {message_type} message detected...
...
```
{{% endtab %}}

{{% tab title="Generating Message from MycroftSkill" %}}
```python
...
def some_method(self):
    self.emitter.emit(Message('{message_type}'{message_data_generating}))
...
```
{{% endtab %}}

{{% tab title="Command line invocation" %}}
```bash
python3 -m mycroft.messagebus.send '{message_type}' {message_data_bash}
```
{{% endtab %}}
{{% endtabs %}}
""",
}


def ingest_csv(filename):
    categories = list()
    data = list()

    def add_category(category):
        new_category = dict()
        new_category[category] = list()
        categories.append(category)
        data.append(new_category)

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t", quotechar='"')
        for row in reader:
            if len(row) <= 0:
                continue
            elif len(row) < 6:
                # Ensure row is standard length
                row = row + [""] * (6 - len(row))

            category = row[0]
            if category not in categories:
                add_category(category)
            category_index = categories.index(category)
            data[category_index][category].append(row[1:])

    return data


def create_markdown(data):
    markdown = str()
    markdown += template["page"]["header"]

    def create_message_data_generating(message_data):
        return (
            ", \n"
            + " " * 30
            + message_data.replace("\n    ", "", 1)
            .replace("\n    ", "\n" + " " * 31)
            .replace("\n}", "}")
        )

    def create_message_data_bash(message_data):
        return "'{}'".format(message_data).replace("\n", "").replace("    ", " ")

    def create_message_handler_title(message_type):
        return "handler_{}".format(message_type.split(":")[-1].replace(".", "_"))

    def listify_items_from_string(items_string):
        """ Convert strings intended to be lists into HTML paragraphs
        """
        if items_string == "":
            return items_string
        # Split string on known delimiters
        items_list = items_string.replace(" / ", "\n").split("\n")
        listed_items = []
        for item in items_list:
            item = item.strip()
            file_extensions = [".py", ".sh"]
            if item[-3:] in file_extensions:
                item = "<code>{}</code>".format(item)
            # TODO probably should abstract this one off
            if item == "CLI (client/text/main.py)":
                item = "CLI (<code>client/text/main.py</code>)"
            item = "<p>{}</p>".format(item)
            listed_items.append(item)

        listed_items = "\n        ".join(listed_items)

        return listed_items

    for category_dict in data:
        category_title = list(category_dict.keys())[0]

        markdown += template["category"]["header"].format(category=category_title)

        for message in category_dict[category_title]:
            message_type, message_data, producer, consumer, description = message
            # Custom formatting for different snippets
            message_handler_title = create_message_handler_title(message_type)
            message_data_generating = ""
            message_data_bash = ""
            if message_data != "":
                message_data_generating = create_message_data_generating(message_data)
                message_data_bash = create_message_data_bash(message_data)
            consumer = listify_items_from_string(consumer)
            producer = listify_items_from_string(producer)

            markdown += template["message"]["header"].format(
                message_type=message_type, description=description
            )
            if message_data != "":
                markdown += template["message"]["data"].format(
                    message_data=message_data
                )
            if producer != "" or consumer != "":
                markdown += template["message"]["actors"].format(
                    producer=producer, consumer=consumer
                )
            markdown += template["message"]["usage"].format(
                message_type=message_type,
                message_handler_title=message_handler_title,
                message_data=message_data,
                message_data_generating=message_data_generating,
                message_data_bash=message_data_bash,
            )

    return markdown


def write_to_file(data, filename):
    with open(filename, "w") as f:
        print(data, file=f)


csv_data = ingest_csv(csv_input_filename)
markdown = create_markdown(csv_data)

write_to_file(markdown, "output.md")
