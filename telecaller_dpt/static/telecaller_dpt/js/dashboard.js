document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.draggable-card');
  const zones = document.querySelectorAll('.status-zone');

  let draggedCard = null;

  cards.forEach(card => {
    card.addEventListener('dragstart', () => {
      draggedCard = card;
      setTimeout(() => card.classList.add('invisible'), 0);
    });

    card.addEventListener('dragend', () => {
      card.classList.remove('invisible');
      draggedCard = null;
    });
  });

  zones.forEach(zone => {
    zone.addEventListener('dragover', e => e.preventDefault());

    zone.addEventListener('dragenter', e => {
      e.preventDefault();
      zone.classList.add('drag-over');
    });

    zone.addEventListener('dragleave', () => zone.classList.remove('drag-over'));

    zone.addEventListener('drop', () => {
      if (draggedCard) {
        const badge = draggedCard.querySelector('.badge');
        const status = zone.dataset.status;
    
        badge.textContent = zone.textContent;
        badge.className = `badge badge-${status}`;
        
        zone.classList.remove('drag-over');
      }
    });
  });
});


