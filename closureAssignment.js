function clickCounter() {
  let clickCount = 0;

  function updateClickCount() {
    clickCount++;
    console.log(`Button clicked ${clickCount} times`);
  }

  return updateClickCount;
}

const clickCounter = clickCounter();

clickCounter();
clickCounter();