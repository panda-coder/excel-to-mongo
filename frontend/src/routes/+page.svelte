<script>
	import { goto } from '$app/navigation';
	let search = ''

	function handleSubmit() {
		goto('/search?t='+search) 
	}
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center">
		<h2 class="font-bold">Welcome.</h2>

		<form on:submit|preventDefault={handleSubmit}>
			<input type="text" placeholder="Content..."  bind:value={search}/>
		  
			<button type="submit">Search</button>
		  </form>
		
	</div>

	<style lang="postcss">
		figure {
			@apply flex relative flex-col;
		}
		figure svg,
		.img-bg {
			@apply w-64 h-64 md:w-80 md:h-80;
		}
		.img-bg {
			@apply bg-gradient-to-r from-primary-300 to-warning-300;
			@apply absolute z-[-1] rounded-full blur-[64px];
			animation: pulse 5s cubic-bezier(0, 0, 0, 0.5) infinite;
		}
		@keyframes pulse {
			50% {
				transform: scale(1.5);
			}
		}
	</style>
</div>
