return {
  {
    "ramojus/mellifluous.nvim",
    opts = {
      mellifluous = {
        highlight_overrides = {
          dark = function(highlighter, colors)
            highlighter.set("VertSplit", { fg = colors.ui_blue })
            highlighter.set("StatusLine", { bg = colors.blue:darkened(20) })
            highlighter.set("SnacksIndent", { fg = colors.ui_blue:darkened(10) })
            highlighter.set("SnacksIndentScope", { fg = colors.ui_purple })
          end,
        },
        color_overrides = {
          dark = {
            bg = function(bg)
              return bg:lightened(4)
            end,
            fg = function(fg)
              return fg:darkened(4)
            end,
            colors = function(colors)
              return {
                fg4 = colors.blue,
                fg5 = colors.fg:darkened(8),
                comments = colors.yellow,
                bg4 = colors.bg:lightened(20),
              }
            end,
          },
        },
      },
    },
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "mellifluous",
    },
  },
}
