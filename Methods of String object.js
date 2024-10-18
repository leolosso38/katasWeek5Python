function splitAndMerge(string, separator) {
  
    // Dividir la cadena en palabras
    const words = string.split(" ");
    
    // Mapear cada palabra, dividirla en caracteres y unir con el separador especificado
    const modifiedWords = words.map(word => {
        return word.split("").join(separator);
    });
    
    // Unir las palabras modificadas de nuevo en una sola cadena con espacios
    return modifiedWords.join(" ");
}