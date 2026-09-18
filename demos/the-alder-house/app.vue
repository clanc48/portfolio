<script setup lang="ts">
const schema={"@context":"https://schema.org","@type":"Hotel","name":"The Alder House","description":"Portfolio demo boutique hotel.","url":"https://example.com/"};
useHead({
  meta:[{name:'description',content:'Portfolio-demo boutique hotel focused on quiet rooms, local experiences, and thoughtful hospitality.'}],
  script:[{type:'application/ld+json',innerHTML:JSON.stringify(schema)}]
})
</script>
<template>
  <div>
    <a class="skipLink" href="#main">Skip to content</a>
    <header class="header container">
      <NuxtLink class="brand" to="/"><span class="monogram">A</span><span>THE ALDER HOUSE<small>A QUIETER KIND OF LUXURY</small></span></NuxtLink>
      <nav class="nav" aria-label="Primary"><NuxtLink to="/rooms">Rooms</NuxtLink><NuxtLink to="/experiences">Experiences</NuxtLink><NuxtLink to="/journal">Journal</NuxtLink></nav>
      <NuxtLink class="button" to="/book">Book your stay</NuxtLink>
    </header>
    <main id="main"><NuxtPage/></main>
    <footer class="footer"><div class="container footerGrid"><div><strong>The Alder House</strong><p>Stay. Explore. Unwind.</p></div><div>Portfolio demo · not a real hotel</div></div></footer>
  </div>
</template>
