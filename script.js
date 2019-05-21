/* globals Docute */

new Docute({
  target: '#docute',
  sourcePath: './docs/',
  nav: [
    {
      title: 'Home',
      link: '/'
    },
    {
      title: 'About',
      link: '/publish'
    },
    {
      title: 'License',
      link: '/license'
    },

    // A dropdown menu
    {
      title: 'Community',
      children: [
        {
          title: 'Spectrum',
          link: 'https://spectrum.chat/your-community'
        },
        {
          title: 'Discord',
          link: 'https://discord.app/your-discord-server'
        }
      ]
    },
    {
      title: '2019',
      children: [
        {
          title: '109w',
          link: '/2019/109w'
        },
        {
          title: '108w',
          link: '/2019/108w'
        },
      ]
    },
  ],

  sidebar: [
    {
      title: 'Guide',
      links: [
        {
          title: 'Introduction',
          link: '/introduction'
        },
        {
          title: 'Installation',
          link: '/installation'
        }
      ]
    },
    {
      title: '2019',
      links: [
        {
          title: '109w',
          link: '/109w'
        },
        {
          title: '108w',
          link: '/108w'
        },
        {
          title: '107w',
          link: '/107w'
        },
      ]
    },

  ],

})
