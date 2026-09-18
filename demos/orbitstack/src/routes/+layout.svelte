<script lang="ts">
 import '../app.css';
 let { children } = $props();
 const schema={"@context":"https://schema.org","@type":"SoftwareApplication","name":"OrbitStack","applicationCategory":"DeveloperApplication","description":"Portfolio demo SaaS platform.","url":"https://example.com/"};
</script>
<svelte:head>
 <meta name="description" content="Portfolio-demo infrastructure SaaS for deploys, observability, environments, and operational control." />
 <script type="application/ld+json">{JSON.stringify(schema)}</script>
</svelte:head>
<a class="skipLink" href="#main">Skip to content</a>
<header class="header container">
 <a class="brand" href="/"><span class="orbit"></span><span>OrbitStack</span></a>
 <nav aria-label="Primary"><a href="/product">Product</a><a href="/solutions">Solutions</a><a href="/pricing">Pricing</a><a href="/docs">Docs</a></nav>
 <a class="button" href="/pricing">Start building</a>
</header>
<main id="main">{@render children()}</main>
<footer class="footer container"><div><strong>OrbitStack</strong><p>The modern stack for what’s next.</p></div><div>Portfolio demo · not a real SaaS product</div></footer>
