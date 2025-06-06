/**
 * All of these values are used throughout the site – for example, 
 * in the <meta> tags, in the footer, and in the RSS feed.
 * 
 * PLEASE BE SURE TO UPDATE THEM ALL! Thank you!
 **/ 

export const siteTitle = 'Distributed System Blog'
export const siteDescription = 'Learn about distributed system'
export const siteURL = 'distributedsystem.netlify.app'
export const siteLink = 'https://github.com/josh-collinsworth/sveltekit-blog-starter'
export const siteAuthor = '- KuroHere'

// Controls how many posts are shown per page on the main blog index pages
export const postsPerPage = 10

// Edit this to alter the main nav menu. (Also used by the footer and mobile nav.)
export const navItems = [
	{ title: 'Home', route: '/' },
	{ title: 'Plan', route: '/plan' },
	{ title: 'Infomation Exchange', route: '/information_exchange' },
	{ title: 'Process & Flow', route: '/process&flow' },
	{ title: 'Prepare', route: '/prepare' },
	{ title: 'Architecture', route: 'architecture' }
];
  