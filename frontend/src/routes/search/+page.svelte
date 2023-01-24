
<script>
   /** @type {import('./$types').PageData} */
  export let data;
  console.log(data)
</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center">
		<h2 class="font-bold">Results for <i>"{data.text}"</i></h2>

		<table>
            <thead>
              <tr>
                <th>File</th>
                <th>Line Nº</th>
                <th>Sheet</th>
                <th>Content</th>
              </tr>
            </thead>
            <tbody>
                
                {#each data.content as item, i}
                <tr>
                    <td><a href="/file/{item.hash}">{item.file}</a></td>
                    <td>{item.line_number}</td>
                    <td>{item.ws_title}</td>
                    <td>{item.content}</td>
                </tr>
                {/each}
            </tbody>
            <tfoot>
            </tfoot>
        </table>
		
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

<style>
    thead > tr {
        background-color: rgba(242, 242,242, 0.5);
    }
    tbody > tr:nth-child(odd) {
        background-color: rgba(100, 100,100 , 0.8);
    }
    tbody > tr:nth-child(even) {
        background-color: rgba(100, 100,100 , 0.8);
    }
</style>
