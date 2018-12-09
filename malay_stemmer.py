import string

# prefixes
prefixes_0 = ['pe', 'pen', 'pem', 'peng', 'peny', 'penge', 'me', 'men', 'mem', 'meng', 'meny', 'menge']
prefixes_1 = ['antar', 'anti', 'eka', 'eks', 'ekstra', 'kau', 'ku', 'maha', 'oto', 'para', 'pasca', 'ultra']
prefixes_2 = ['ber', 'per', 'ter', 'memper', 'diper']
prefixes_3 = ['se', 'di', 'ke', 'te', 'pem', 'bel', 'pel', 'juru', 'berke']

# suffixes
suffixes_all = 'kan i an ku mu nya kau kah lah tah nda wan wati man ita pun isme kannya inya'.split()

# known circumfixes
prefix_suffix_list = {
    'pe':     ['an', 'i'],  # (noun)
    'pen':    ['an', 'i'],  # (noun)
    'pem':    ['an', 'i'],  # (noun)
    'peng':   ['an', 'i'],  # (noun)
    'peny':   ['an', 'i'],  # (noun)
    'penge':  ['an', 'i'],  # (noun)
    'me':     ['kan', 'i'],  # (verb)
    'men':    ['kan', 'i', 'inya'],  # (verb)
    'mem':    ['kan', 'i'],  # (verb)
    'meng':   ['kan', 'i'],  # (verb)
    'meny':   ['kan', 'i'],  # (verb)
    'menge':  ['kan', 'i'],  # (verb)

    'antar':  [],  # inter-
    'anti':   [],  # anti-
    'eka':    [],  # mono-
    'eks':    [],  # ex-
    'ekstra': [],  # extra-
    'kau':    [],  # you-shall-
    'ku':     [],  # I-myself-
    'maha':   [],  # extremely-
    'oto':    [],  # auto-
    'para':   [],  # para-
    'pasca':  [],  # post-
    'ultra':  [],  # ultra-

    'ber':    ['an', 'kan'],  # (trait)
    'per':    ['kan', 'an', 'i'],
    'ter':    ['kan', 'i'],  # (state)
    'memper': ['kan', 'i'],
    'diper':  ['kan', 'i', 'kannya'],

    'se':     ['an', 'nya'],  # (singleton)
    'di':     ['kan', 'i', 'kannya'],  # (adverb)
    'ke':     ['an', 'i'],
    'te':     ['an'],
    'bel':    [],
    'pel':    ['an'],
    'juru':   [],
    'berke':  ['an'],
}

# ignore since infixing is so rare and the words are totally different
infixes = {'el', 'em', 'er', 'en', 'in'}


def flatten(list_of_lists):
    return [item for sub_list in list_of_lists for item in sub_list]


# assert prefix lists are comprehensive
assert all(prefix in prefix_suffix_list.keys() for prefix in prefixes_0 + prefixes_1 + prefixes_2 + prefixes_3)

# assert prefix_suffix list is comprehensive
assert all(prefix in prefixes_0 + prefixes_1 + prefixes_2 + prefixes_3 for prefix in prefix_suffix_list.keys())
assert all(suffix in suffixes_all for suffix in flatten(prefix_suffix_list.values()))

# ignore
illegal_starting_bigrams = ['aa', 'aq', 'ax', 'bb', 'bc', 'bd', 'bf', 'bg', 'bj', 'bk', 'bm', 'bn', 'bp', 'bq', 'bv',
                            'bw', 'bx', 'bz', 'cb', 'cc', 'cd', 'cf', 'cg', 'cj', 'ck', 'cn', 'cp', 'cq', 'cr', 'cs',
                            'ct', 'cv', 'cw', 'cx', 'cy', 'db', 'dc', 'dd', 'df', 'dh', 'dj', 'dk', 'dm', 'dn', 'dp',
                            'dq', 'dt', 'dx', 'dy', 'dz', 'ea', 'ee', 'eo', 'eq', 'ex', 'ey', 'ez', 'fb', 'fc', 'fd',
                            'ff', 'fg', 'fh', 'fj', 'fk', 'fm', 'fn', 'fp', 'fq', 'fs', 'ft', 'fv', 'fw', 'fx', 'fy',
                            'fz', 'gb', 'gc', 'gd', 'gf', 'gg', 'gj', 'gk', 'gp', 'gq', 'gs', 'gt', 'gv', 'gw', 'gx',
                            'gy', 'gz', 'hc', 'hd', 'hf', 'hg', 'hj', 'hk', 'hl', 'hn', 'hp', 'hq', 'hr', 'hs', 'ht',
                            'hv', 'hw', 'hx', 'hy', 'hz', 'ic', 'ie', 'ii', 'iq', 'iv', 'iw', 'ix', 'jb', 'jc', 'jd',
                            'jf', 'jg', 'jh', 'jj', 'jk', 'jl', 'jm', 'jn', 'jp', 'jq', 'jr', 'js', 'jt', 'jv', 'jw',
                            'jx', 'jy', 'jz', 'kb', 'kc', 'kf', 'kj', 'kk', 'kp', 'kq', 'ks', 'kt', 'kv', 'kw', 'kx',
                            'ky', 'kz', 'lc', 'ld', 'lf', 'lg', 'lh', 'lj', 'lk', 'll', 'lm', 'ln', 'lp', 'lq', 'lr',
                            'ls', 'lt', 'lv', 'lw', 'lx', 'ly', 'lz', 'mb', 'mc', 'md', 'mf', 'mg', 'mh', 'mj', 'mk',
                            'ml', 'mq', 'mt', 'mv', 'mw', 'mx', 'mz', 'nb', 'nc', 'nd', 'nf', 'nj', 'nk', 'nl', 'nm',
                            'nn', 'np', 'nq', 'nr', 'ns', 'nt', 'nv', 'nw', 'nx', 'nz', 'oe', 'oo', 'oq', 'ow', 'ox',
                            'pb', 'pc', 'pf', 'pg', 'ph', 'pj', 'pk', 'pm', 'pp', 'pq', 'pt', 'pv', 'pw', 'px', 'pz',
                            'qb', 'qc', 'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp',
                            'qq', 'qr', 'qs', 'qt', 'qu', 'qv', 'qw', 'qx', 'qy', 'qz', 'rb', 'rc', 'rd', 'rf', 'rg',
                            'rh', 'rj', 'rk', 'rl', 'rm', 'rp', 'rq', 'rr', 'rs', 'rt', 'rv', 'rw', 'rx', 'ry', 'rz',
                            'sb', 'sd', 'sg', 'sh', 'sq', 'ss', 'sv', 'sx', 'sz', 'tc', 'td', 'tf', 'tg', 'tj', 'tk',
                            'tl', 'tm', 'tn', 'tp', 'tq', 'tv', 'tw', 'tx', 'ty', 'tz', 'ue', 'uh', 'uq', 'uu', 'uv',
                            'uw', 'ux', 'uy', 'vb', 'vc', 'vd', 'vf', 'vg', 'vh', 'vj', 'vk', 'vl', 'vm', 'vn', 'vp',
                            'vq', 'vr', 'vs', 'vt', 'vv', 'vw', 'vx', 'vy', 'vz', 'wb', 'wc', 'wd', 'wf', 'wg', 'wj',
                            'wk', 'wl', 'wm', 'wn', 'wp', 'wq', 'ws', 'wt', 'wv', 'ww', 'wx', 'wy', 'wz', 'xb', 'xc',
                            'xd', 'xf', 'xg', 'xh', 'xj', 'xk', 'xl', 'xm', 'xn', 'xo', 'xp', 'xq', 'xr', 'xs', 'xt',
                            'xu', 'xv', 'xw', 'xx', 'xy', 'xz', 'yb', 'yc', 'yd', 'yf', 'yh', 'yj', 'yk', 'yl', 'ym',
                            'yn', 'yp', 'yq', 'yr', 'ys', 'yt', 'yv', 'yw', 'yx', 'yy', 'yz', 'zb', 'zc', 'zd', 'zf',
                            'zg', 'zh', 'zj', 'zk', 'zl', 'zm', 'zn', 'zp', 'zq', 'zr', 'zs', 'zt', 'zv', 'zw', 'zx',
                            'zy', 'zz']

# ignore
illegal_ending_bigrams = ['av', 'ax', 'bb', 'bd', 'bf', 'bg', 'bh', 'bj', 'bk', 'bl', 'bm', 'bn', 'bp', 'bq', 'br',
                          'bs', 'bv', 'bw', 'bx', 'by', 'bz', 'cb', 'cc', 'cd', 'cf', 'cg', 'cj', 'cl', 'cn', 'cp',
                          'cq', 'cr', 'cs', 'ct', 'cv', 'cw', 'cx', 'cz', 'db', 'dc', 'dd', 'df', 'dg', 'dh', 'dj',
                          'dk', 'dl', 'dm', 'dn', 'dp', 'dq', 'dr', 'ds', 'dt', 'dv', 'dw', 'dx', 'dz', 'ec', 'eq',
                          'eu', 'ev', 'ex', 'ez', 'fb', 'fc', 'fd', 'fg', 'fh', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo',
                          'fp', 'fq', 'fr', 'fs', 'ft', 'fv', 'fw', 'fx', 'fy', 'fz', 'gb', 'gc', 'gd', 'gf', 'gg',
                          'gj', 'gk', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gv', 'gw', 'gx', 'gy', 'gz', 'hc', 'hd',
                          'hf', 'hj', 'hk', 'hl', 'hp', 'hq', 'hr', 'ht', 'hv', 'hw', 'hx', 'hy', 'hz', 'iv', 'iw',
                          'ix', 'iy', 'jb', 'jc', 'jd', 'jf', 'jg', 'jh', 'jj', 'jk', 'jl', 'jm', 'jn', 'jp', 'jq',
                          'jr', 'js', 'jt', 'jv', 'jw', 'jx', 'jy', 'jz', 'kb', 'kc', 'kd', 'kf', 'kj', 'kk', 'kl',
                          'kn', 'kp', 'kq', 'kr', 'kt', 'kv', 'kw', 'kx', 'ky', 'kz', 'lc', 'lg', 'lj', 'lq', 'lr',
                          'lv', 'lw', 'lx', 'lz', 'mb', 'mc', 'md', 'mf', 'mg', 'mh', 'mj', 'mk', 'ml', 'mn', 'mq',
                          'mr', 'mt', 'mv', 'mw', 'mx', 'my', 'mz', 'nb', 'nf', 'nh', 'nj', 'nm', 'nn', 'np', 'nq',
                          'nr', 'nv', 'nw', 'nx', 'nz', 'oj', 'oq', 'ov', 'ow', 'oy', 'oz', 'pb', 'pc', 'pf', 'pg',
                          'pj', 'pk', 'pl', 'pm', 'pn', 'pp', 'pq', 'pt', 'pv', 'pw', 'px', 'py', 'pz', 'qb', 'qc',
                          'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp', 'qq', 'qr',
                          'qs', 'qt', 'qu', 'qv', 'qw', 'qx', 'qy', 'qz', 'rc', 'rh', 'rj', 'rp', 'rq', 'rr', 'rv',
                          'rw', 'rx', 'rz', 'sc', 'sd', 'sf', 'sg', 'sl', 'sm', 'sn', 'sp', 'sq', 'sr', 'ss', 'sv',
                          'sw', 'sx', 'sz', 'tc', 'td', 'tf', 'tg', 'tj', 'tn', 'tp', 'tq', 'tv', 'tw', 'ty', 'uc',
                          'uq', 'uu', 'uv', 'uw', 'ux', 'uy', 'vb', 'vc', 've', 'vf', 'vg', 'vh', 'vj', 'vk', 'vl',
                          'vm', 'vn', 'vp', 'vq', 'vr', 'vs', 'vt', 'vu', 'vv', 'vw', 'vx', 'vy', 'vz', 'wb', 'wc',
                          'wd', 'wf', 'wg', 'wh', 'wj', 'wk', 'wl', 'wm', 'wn', 'wp', 'wq', 'wr', 'ws', 'wt', 'wu',
                          'wv', 'ww', 'wx', 'wy', 'wz', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf', 'xg', 'xh', 'xi', 'xj',
                          'xk', 'xl', 'xm', 'xn', 'xo', 'xp', 'xq', 'xr', 'xs', 'xt', 'xu', 'xv', 'xw', 'xx', 'xy',
                          'xz', 'yb', 'yc', 'yd', 'yf', 'yg', 'yh', 'yj', 'yk', 'yl', 'ym', 'yn', 'yp', 'yq', 'ys',
                          'yt', 'yv', 'yw', 'yx', 'yy', 'yz', 'zb', 'zc', 'zd', 'zf', 'zg', 'zh', 'zj', 'zk', 'zl',
                          'zm', 'zn', 'zo', 'zp', 'zq', 'zr', 'zs', 'zt', 'zu', 'zv', 'zw', 'zx', 'zy', 'zz']


def is_single_syllable(word):
    char_seq = ''.join(['0' if char in 'aeiou' else '1' for char in word])
    return char_seq in '10 100 101 110 1000 1001 1011 1100 1101'


def stem_prefix(word):
    """
    yields all possible stemmings
    :return: (root, prefix)
    """

    # simple case:
    yield word, ''

    # check length
    if len(word) > 3:

        # very special case prefixes
        if word.startswith('pe') or word.startswith('me'):

            # single syllable pattern ==> prefix: penge
            if word[2:].startswith('nge'):
                if len(word) > 6 and is_single_syllable(word[5:]):
                    yield word[5:], word[:5]

            # root init: s ==> prefix: peny
            if len(word) > 4 and word[2:].startswith('ny'):

                # normal match
                if word[4] == 's':
                    yield word[4:], word[:4]

                # s undelete for legal bigrams
                if word[4] in string.ascii_lowercase.replace('s', ''):
                    yield 's' + word[4:], word[:4]

            # root init: a e i o u g h k ==> prefix: peng
            if len(word) > 4 and word[2:].startswith('ng'):

                # normal match
                if word[4] in 'aeioughk':
                    yield word[4:], word[:4]

                # k undelete for legal bigrams
                if word[4] in string.ascii_lowercase.replace('k', ''):
                    yield 'k' + word[4:], word[:4]

            # root init: b f v p ==> prefix: pem
            if len(word) > 3 and word[2:].startswith('m'):

                # normal match
                if word[3] in 'bfvp':
                    yield word[3:], word[:3]

                # p undelete for legal bigrams
                if word[3] in string.ascii_lowercase.replace('p', ''):
                    yield 'p' + word[3:], word[:3]

            # root init: c d j t ==> prefix: pen
            if len(word) > 3 and word[2:].startswith('n'):

                # normal match
                if word[3] in 'cdjt':
                    yield word[3:], word[:3]

                # t undelete for legal bigrams
                if word[3] in string.ascii_lowercase.replace('t', ''):
                    yield 't' + word[3:], word[:3]

            # root init: l m n q r w x y z ==> prefix: pe
            if word[2] in 'lmnqrwxyz':
                yield word[2:], word[:2]

            # sometimes the rules aren't followed, eg. pe-periksa-an
            else:
                yield word[2:], word[:2]

        # prefixes stolen from english
        for prefix in prefixes_1:
            if word.startswith(prefix):
                yield word[len(prefix):], prefix

        # r-removed prefixes
        for prefix in prefixes_2:
            if len(word) > len(prefix) and word.startswith(prefix):
                # normal match
                yield word[len(prefix):], prefix

                # r undelete for legal bigrams
                if word[len(prefix)] in string.ascii_lowercase.replace('r', ''):
                    yield 'r' + word[len(prefix):], prefix

        # other prefixes
        for prefix in prefixes_3:
            if word.startswith(prefix):
                yield word[len(prefix):], prefix


def stem_suffix(word, prefix):
    """
    yields all possible stemmings
    :return: (root, prefix, suffix)
    """

    # simple case
    yield word, prefix, ''

    # find valid suffixes
    if prefix == '':
        suffixes = suffixes_all
    else:
        suffixes = prefix_suffix_list[prefix]

    # test each
    for suffix in suffixes:
        if word.endswith(suffix):
            yield word[:-len(suffix)], prefix, suffix


def stem(word, recursive=False):
    """
    yields all possible stemmings
    includes original word
    includes split by dash
    optional recursive descent
    :return: (root, prefix, suffix)
    """
    if word.count('-') == 1:
        word_1, word_2 = word.split('-')
        word_1_stemmings = set(stem(word_1, recursive))
        word_2_stemmings = set(stem(word_2, recursive))
        for root_1, prefix_1, suffix_1 in word_1_stemmings:
            for root_2, prefix_2, suffix_2 in word_2_stemmings:
                if root_1 == root_2:
                    # both equally affixed
                    if (prefix_1, suffix_1) == (prefix_2, suffix_2):
                        yield root_2, prefix_1, suffix_2
                    # or the entire thing affixed as a whole
                    elif not suffix_1 and not prefix_2:
                        yield root_2, prefix_1, suffix_2
                    # only the first word is affixed
                    elif not prefix_2 and not suffix_2:
                        # yield root_2, prefix_1, suffix_1
                        pass  # doesn't ever seem to happen
                    # only the second word is affixed
                    elif not prefix_1 and not suffix_1:
                        yield root_2, prefix_2, suffix_2
    elif all(char in string.ascii_lowercase for char in word.lower()):
        for word_prefix_pair in stem_prefix(word):
            for root, prefix, suffix in stem_suffix(*word_prefix_pair):
                # recursive call
                if recursive and root and (prefix or suffix):
                    for recursive_root, recursive_prefix, recursive_suffix in stem(root, recursive):
                        # will not start with illegal bigrams
                        yield recursive_root, prefix + recursive_prefix, recursive_suffix + suffix
                # recursion termination
                elif root and root[:2] not in illegal_starting_bigrams and root[-2:] not in illegal_ending_bigrams:
                    yield root, prefix, suffix
                    pass
    else:
        print('I expect all lowercase with at most one dash!')


if __name__ == '__main__':
    for word in ['menggelisahi', 'rim', 'meredup', 'dibeli', 'gerugut', 'momake', 'mengaram', 'merawati', 'tambahan',
                 'spora', 'gol', 'kegiliran', 'cermat', 'adun', 'kehematan', 'mencetekkan', 'komen', 'aorta', 'usia',
                 'menggandakan', 'berbadai', 'tilikan', 'langsai', 'gapai', 'membran', 'hornblend', 'pemotong',
                 'kelian', 'pengiring', 'ijuk', 'melucutkan', 'seraha', 'psikedelik', 'berwajah', 'sungkum',
                 'kegayatan', 'songkok', 'menggeritik', 'ketewasan', 'gin', 'khatam', 'membau', 'menempel', 'pejoratif',
                 'pergedel', 'menggagau', 'memuncungkan', 'menghempaskan', 'menggilaskan', 'menghablur', 'dusin',
                 'mengingati', 'murai', 'pirau', 'perkilangan', 'tamtama', 'tetumbuhan', 'keasistenan', 'ditadbir',
                 'surau', 'gajus', 'mencita-citakan', 'disember', 'berkeley']:
        print('', word, '-->', set(stem(word, recursive=True)))

    while 1:
        search_query = input('WORD TO STEM:\n')
        if not search_query:
            break
        results = sorted(set(stem(search_query)), key=lambda x: len(x[0]))
        print('found %d items' % len(results))
        print('', search_query, '-->', results)
        results = sorted(set(stem(search_query, recursive=True)), key=lambda x: len(x[0]))
        print('found %d items (recursive)' % len(results))
        print('', search_query, '-->', results)
