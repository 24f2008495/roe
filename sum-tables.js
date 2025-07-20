const { chromium } = require('playwright');

const seeds = Array.from({ length: 10 }, (_, i) => 76 + i);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  let total = 0;

  for (const seed of seeds) {
    const url = `https://sanand0.github.io/tdsdata/js_table/?seed=${seed}`;
    await page.goto(url);
    const numbers = await page.$$eval("table td", cells =>
      cells.map(cell => parseFloat(cell.innerText)).filter(n => !isNaN(n))
    );
    const pageSum = numbers.reduce((a, b) => a + b, 0);
    console.log(`Seed ${seed} sum:`, pageSum);
    total += pageSum;
  }

  console.log("TOTAL SUM:", total);
  await browser.close();
})();
