import argparse, sqlite3, sys

from ..api import to_token_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sqlite', type=str)
    args = parser.parse_args()

    token_set = set()
    for line in sys.stdin:
        token_list = to_token_list(line)
        for t in token_list:
            if not t in token_set: 
                token_set.add(t)
                print(t)

    if args.sqlite:
        insert_tokens(args.sqlite, sorted(token_set))

def insert_tokens(db_path: str, token_set: set[str]):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute('BEGIN TRANSACTION;')

        sql_create_table = '''
            CREATE TABLE IF NOT EXISTS t_raw_token (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT NOT NULL UNIQUE
            );
        '''
        cur.execute(sql_create_table)

        sql_insert = '''
            INSERT OR IGNORE INTO t_raw_token (
                token
            ) VALUES (
                ?
            );
        '''
        for token in token_set:
            cur.execute(sql_insert, (token,))
    except sqlite3.Error as e:
        con.rollback()
        raise e 
    else:
        con.commit()

if __name__ == '__main__':
    main()
