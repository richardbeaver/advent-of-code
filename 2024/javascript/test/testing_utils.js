/**
 * Extracts the day that the given file is for based on its name
 * @param {string} filename
 * @returns {number}
 */
function getDayFromFileName(filename) {
  const re = /day(\d+)/;
  const match = re.exec(filename);

  if (match === null) {
    throw new Error(`Could not extract day from filename: ${filename}`);
  }
  return Number(match[1]);
}

module.exports = { getDayFromFileName };
