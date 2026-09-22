(function () {
  "use strict";

  var CONTENT_ROOT = "content/";
  var els = {};
  var manifest = [];      // [{path, title, section}]
  var searchIndex = [];   // [{path, title, text}]
  var tree = {};          // nested tree built from manifest paths

  document.addEventListener("DOMContentLoaded", init);

  function init() {
    els.fileTree = document.getElementById("file-tree");
    els.article = document.getElementById("article");
    els.breadcrumb = document.getElementById("breadcrumb");
    els.searchInput = document.getElementById("search-input");
    els.searchResults = document.getElementById("search-results");
    els.sidebar = document.getElementById("sidebar");
    els.sidebarToggle = document.getElementById("sidebar-toggle");

    els.sidebarToggle.addEventListener("click", function () {
      els.sidebar.classList.toggle("open");
    });

    els.searchInput.addEventListener("input", onSearchInput);
    els.searchInput.addEventListener("focus", function () {
      if (els.searchInput.value.trim()) els.searchResults.hidden = false;
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search-wrap")) els.searchResults.hidden = true;
    });

    window.addEventListener("hashchange", route);

    Promise.all([
      fetchJSON("assets/data/manifest.json"),
      fetchJSON("assets/data/search-index.json")
    ]).then(function (results) {
      manifest = results[0];
      searchIndex = results[1];
      tree = buildTree(manifest);
      renderTree();
      route();
    }).catch(function (err) {
      els.fileTree.textContent = "Failed to load directory listing.";
      els.article.innerHTML = "<p>Could not load site data (" + escapeHtml(String(err)) + "). If you're browsing this on GitHub Pages, try reloading.</p>";
    });
  }

  function fetchJSON(path) {
    return fetch(path).then(function (r) {
      if (!r.ok) throw new Error(r.status + " " + path);
      return r.json();
    });
  }

  function buildTree(items) {
    var root = { type: "folder", name: "", path: "", children: {} };
    items.forEach(function (item) {
      var parts = item.path.split("/");
      var node = root;
      for (var i = 0; i < parts.length; i++) {
        var part = parts[i];
        var isFile = i === parts.length - 1;
        if (isFile) {
          node.children[part] = { type: "file", name: part, path: item.path, title: item.title };
        } else {
          if (!node.children[part]) {
            node.children[part] = {
              type: "folder",
              name: part,
              path: parts.slice(0, i + 1).join("/"),
              children: {}
            };
          }
          node = node.children[part];
        }
      }
    });
    return root;
  }

  function renderTree() {
    els.fileTree.innerHTML = "";
    var ul = renderFolderChildren(tree, 0);
    els.fileTree.appendChild(ul);
  }

  function folderLabel(name) {
    return name.replace(/^\d+[-.]?\s*/, "").replace(/-/g, " ");
  }

  function fileLabel(node) {
    if (node.title) return node.title;
    return node.name.replace(/\.md$/, "").replace(/^\d+[-.]?\s*/, "").replace(/-/g, " ");
  }

  function renderFolderChildren(folderNode, depth) {
    var ul = document.createElement("ul");
    var keys = Object.keys(folderNode.children).sort();
    keys.forEach(function (key) {
      var node = folderNode.children[key];
      var li = document.createElement("li");
      if (node.type === "folder") {
        var label = document.createElement("div");
        label.className = "tree-folder";
        label.innerHTML = '<span class="caret">&#9660;</span><span>' + escapeHtml(folderLabel(node.name)) + "</span>";
        label.dataset.path = node.path;
        var childUl = renderFolderChildren(node, depth + 1);
        label.addEventListener("click", function () {
          label.classList.toggle("collapsed");
        });
        li.appendChild(label);
        li.appendChild(childUl);
      } else {
        var a = document.createElement("a");
        a.className = "tree-file";
        a.href = "#/" + node.path;
        a.textContent = fileLabel(node);
        a.dataset.path = node.path;
        li.appendChild(a);
      }
      ul.appendChild(li);
    });
    return ul;
  }

  function expandToPath(path) {
    if (!path) return;
    var parts = path.split("/");
    parts.pop();
    var acc = [];
    parts.forEach(function (p) {
      acc.push(p);
      var folderPath = acc.join("/");
      var el = els.fileTree.querySelector('.tree-folder[data-path="' + cssEscape(folderPath) + '"]');
      if (el) el.classList.remove("collapsed");
    });
  }

  function cssEscape(s) {
    return s.replace(/["\\]/g, "\\$&");
  }

  function setActiveFile(path) {
    var current = els.fileTree.querySelector(".tree-file.active");
    if (current) current.classList.remove("active");
    if (!path) return;
    var el = els.fileTree.querySelector('.tree-file[data-path="' + cssEscape(path) + '"]');
    if (el) el.classList.add("active");
  }

  function route() {
    var hash = window.location.hash || "#/";
    var path = decodeURIComponent(hash.replace(/^#\/?/, ""));
    els.sidebar.classList.remove("open");
    if (!path) {
      renderHome();
      setActiveFile(null);
      els.breadcrumb.innerHTML = "";
      return;
    }
    loadArticle(path);
  }

  function renderHome() {
    document.title = "Digital Support and Security T Level Wiki";
    var sections = {};
    manifest.forEach(function (item) {
      var top = item.path.split("/")[0];
      sections[top] = sections[top] || [];
      sections[top].push(item);
    });
    var html = "<h1>Digital Support and Security T Level</h1>";
    html += "<p><em>An independent, browsable study-guide wiki for the T Level Technical Qualification in Digital Support and Security (Level 3).</em></p>";
    html += "<p>Use the search bar above, or browse the directory tree on the left &mdash; it mirrors the <code>/content</code> folder in the GitHub repository. Start with the overview, or jump straight to a topic:</p>";
    html += '<div class="home-grid">';
    Object.keys(sections).sort().forEach(function (top) {
      var items = sections[top];
      var first = items[0];
      var isRootFile = top.endsWith(".md");
      var label = isRootFile ? first.title : cap(folderLabel(top));
      html += '<a class="home-card" href="#/' + first.path + '" style="display:block;color:inherit;">';
      html += "<h3>" + escapeHtml(label) + "</h3>";
      html += "<p>" + items.length + " page" + (items.length === 1 ? "" : "s") + "</p>";
      html += "</a>";
    });
    html += "</div>";
    els.article.innerHTML = html;
  }

  function cap(s) {
    return s.replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  function loadArticle(path) {
    els.article.innerHTML = '<p class="loading">Loading&hellip;</p>';
    fetch(CONTENT_ROOT + path)
      .then(function (r) {
        if (!r.ok) throw new Error("404");
        return r.text();
      })
      .then(function (md) {
        var html = window.marked ? window.marked.parse(md) : "<pre>" + escapeHtml(md) + "</pre>";
        els.article.innerHTML = html;
        var h1 = els.article.querySelector("h1");
        document.title = (h1 ? h1.textContent : path) + " - T Level Wiki";
        renderBreadcrumb(path);
        setActiveFile(path);
        expandToPath(path);
        els.article.querySelectorAll("a[href]").forEach(function (a) {
          var href = a.getAttribute("href");
          if (href && !/^([a-z]+:)?\/\//i.test(href) && !href.startsWith("#")) {
            a.setAttribute("href", "#/" + resolveRelative(path, href));
          }
        });
      })
      .catch(function () {
        els.article.innerHTML = "<h1>Page not found</h1><p>No content file at <code>" + escapeHtml(path) + "</code>. Use the directory tree or search to find a page.</p>";
        els.breadcrumb.innerHTML = "";
      });
  }

  function resolveRelative(currentPath, href) {
    href = href.replace(/^\.\//, "");
    var baseParts = currentPath.split("/");
    baseParts.pop();
    var hrefParts = href.split("/");
    hrefParts.forEach(function (part) {
      if (part === "..") baseParts.pop();
      else if (part !== ".") baseParts.push(part);
    });
    return baseParts.join("/");
  }

  function renderBreadcrumb(path) {
    var parts = path.split("/");
    var acc = [];
    var html = '<a href="#/">content</a>';
    parts.forEach(function (part, i) {
      acc.push(part);
      var isLast = i === parts.length - 1;
      var label = isLast ? part : folderLabel(part);
      html += '<span class="sep">/</span>';
      if (isLast) {
        html += "<span>" + escapeHtml(label) + "</span>";
      } else {
        var folderPath = acc.join("/");
        html += '<a href="#/' + folderPath + '" class="bc-folder" data-path="' + folderPath + '">' + escapeHtml(label) + "</a>";
      }
    });
    els.breadcrumb.innerHTML = html;
    els.breadcrumb.querySelectorAll(".bc-folder").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var el = els.fileTree.querySelector('.tree-folder[data-path="' + cssEscape(a.dataset.path) + '"]');
        if (el) el.classList.remove("collapsed");
        var firstChild = els.fileTree.querySelector('.tree-file[data-path^="' + cssEscape(a.dataset.path) + '/"]');
        if (firstChild) window.location.hash = "#/" + firstChild.dataset.path;
      });
    });
  }

  // ---- Search ----
  function onSearchInput() {
    var q = els.searchInput.value.trim().toLowerCase();
    if (!q) {
      els.searchResults.hidden = true;
      els.searchResults.innerHTML = "";
      return;
    }
    var terms = q.split(/\s+/).filter(Boolean);
    var scored = [];
    searchIndex.forEach(function (item) {
      var hay = (item.title + " " + item.text).toLowerCase();
      var score = 0;
      var ok = true;
      terms.forEach(function (t) {
        var idx = hay.indexOf(t);
        if (idx === -1) { ok = false; return; }
        score += (item.title.toLowerCase().indexOf(t) !== -1 ? 10 : 1);
      });
      if (ok) scored.push({ item: item, score: score });
    });
    scored.sort(function (a, b) { return b.score - a.score; });
    scored = scored.slice(0, 15);

    if (!scored.length) {
      els.searchResults.innerHTML = '<div class="sr-empty">No pages match &ldquo;' + escapeHtml(q) + '&rdquo;.</div>';
      els.searchResults.hidden = false;
      return;
    }

    var html = "";
    scored.forEach(function (s) {
      var item = s.item;
      var snippet = buildSnippet(item.text, terms);
      html += '<a href="#/' + item.path + '">';
      html += '<span class="sr-title">' + highlight(item.title, terms) + "</span>";
      html += '<span class="sr-path">' + escapeHtml(item.path) + "</span>";
      if (snippet) html += '<span class="sr-snippet">' + highlight(snippet, terms) + "</span>";
      html += "</a>";
    });
    els.searchResults.innerHTML = html;
    els.searchResults.hidden = false;
    els.searchResults.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { els.searchResults.hidden = true; els.searchInput.value = ""; });
    });
  }

  function buildSnippet(text, terms) {
    var lower = text.toLowerCase();
    var idx = -1;
    for (var i = 0; i < terms.length; i++) {
      idx = lower.indexOf(terms[i]);
      if (idx !== -1) break;
    }
    if (idx === -1) idx = 0;
    var start = Math.max(0, idx - 40);
    var end = Math.min(text.length, idx + 100);
    var snippet = (start > 0 ? "\u2026" : "") + text.slice(start, end) + (end < text.length ? "\u2026" : "");
    return snippet;
  }

  function highlight(text, terms) {
    var escaped = escapeHtml(text);
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig");
      escaped = escaped.replace(re, "<mark>$1</mark>");
    });
    return escaped;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
})();
