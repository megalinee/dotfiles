return {
  "folke/snacks.nvim",
  ---@type snacks.Config
  opts = {
    explorer = {
      -- your explorer configuration comes here
      -- or leave it empty to use the default settings
      -- refer to the configuration section below
    },
    picker = {
      hidden = true,
      ignored = true,
      sources = {
        files = {
          hidden = true,
          ignored = true,
          -- exclude = {
          -- "**/.git/*",
          --},
        },
      },
    },
  },
}
