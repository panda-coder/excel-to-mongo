<script>
	import '@skeletonlabs/skeleton/themes/theme-vintage.css';
	import '@skeletonlabs/skeleton/styles/all.css';
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
</script>

<!-- App Shell -->
<AppShell slotSidebarLeft="bg-surface-500/5 w-56 p-4">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<a class="btn btn-sm btn-ghost-surface" href="/" rel="noreferrer"><strong class="text-xl uppercase">Excel to Mongo</strong></a>
			</svelte:fragment>

			<svelte:fragment slot="trail">
				<a class="btn btn-sm btn-ghost-surface" href="/upload" rel="noreferrer">Cadastrar planilha</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
</AppShell>
