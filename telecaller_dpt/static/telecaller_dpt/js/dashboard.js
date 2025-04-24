document.addEventListener('DOMContentLoaded', function () {
  const zones = document.querySelectorAll('.zone');

  zones.forEach(zone => {
    new Sortable(zone, {
      group: 'cards',
      animation: 150,
      onAdd: function (evt) {
        const card = evt.item;
        const parentZone = zone.parentElement;
        const newStatus = parentZone.getAttribute('data-status');
        const badge = card.querySelector('.badge');

        // Reset badge
        badge.className = 'badge';
        if (newStatus === 'new-lead') badge.classList.add('bg-primary');
        if (newStatus === 'cold-call') badge.classList.add('badge-cold-call');
        if (newStatus === 'follow-up') badge.classList.add('badge-follow-up');
        if (newStatus === 'deal-closed') badge.classList.add('badge-deal-closed');

        badge.textContent = newStatus.replace('-', ' ').replace(/\b\w/g, c => c.toUpperCase());
      }
    });
  });
});
