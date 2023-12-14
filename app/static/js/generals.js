// Função para alternar o tema
function toggleTheme(event) {

    let currentTheme = $('body').attr('data-bs-theme');
    let newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    // Define o novo tema
    $('body').attr('data-bs-theme', newTheme);
 
    let themeDescription = newTheme == 'dark' ? "Tema Escuro" : "Tema Claro";
  
    $(`#${event.id}-caption`).html(themeDescription);
  }