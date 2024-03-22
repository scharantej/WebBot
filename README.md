## Flask Application Design for a Website Builder Using Chat GPT Inputs

### HTML Files

- **index.html:** The main HTML file that serves as the entry point for the website builder. It includes a form that allows users to interact with Chat GPT and build their website.
- **preview.html:** A preview page that dynamically displays the website being built, based on the user's interactions and Chat GPT's inputs.

### Routes

- **`/`:** The root route that renders the **index.html** file.
- **`/build`:** A POST route that handles the form submission from **index.html**. It sends the user's inputs to Chat GPT and receives the website specification.
- **`/preview`:** A GET route that renders the **preview.html** file, passing the website specification received from Chat GPT.