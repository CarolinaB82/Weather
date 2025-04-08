const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,  // Cela reste inchangé
  outputDir: 'dist'  // Ajoute cette ligne pour définir le dossier de sortie
})