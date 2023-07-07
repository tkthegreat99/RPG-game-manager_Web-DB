from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, static_folder='static')

# MySQL 데이터베이스 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="gamemanager"
)

@app.route('/')
def index():
    return render_template('Overview.html')

@app.route('/register-character', methods=['POST'])
def register_character():
    player_email = request.form['player_email']
    character_name = request.form['character-name']
    character_class = request.form['character-class']
    character_gender = request.form['character-gender']

    cursor = db.cursor()
    sql = "INSERT INTO characters (player_email,character_name, character_class, character_gender) VALUES (%s,%s, %s, %s)"
    values = (player_email, character_name, character_class, character_gender)

    try:
        cursor.execute(sql, values)
        db.commit()
        return "New character registered successfully."
    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}"
    finally:
        cursor.close()



@app.route('/find-character', methods=['GET', 'POST'])
def find_character():
    characters = []
    message = ''
    if request.method == 'POST':
        character_name = request.form['name']
        cursor = db.cursor()

        query = "SELECT * FROM characters WHERE character_name = %s"
        cursor.execute(query, [character_name])

        characters = cursor.fetchall()
        cursor.close()
        
        if not characters:  # 결과가 없다면
            message = 'There is no such character'

    return render_template('Characters.html', characters=characters, message=message)

@app.route('/item-list')
def item_list():
    cursor = db.cursor()
    query = "SELECT * FROM item"
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()
    return render_template('Items.html', items=items)

@app.route('/show-quests')
def show_quests():
    cursor = db.cursor()
    query = "SELECT * FROM quests"
    cursor.execute(query)
    quests = cursor.fetchall()
    cursor.close()
    return render_template('Quests.html', quests=quests)
@app.route('/register-quest', methods=['POST'])
def register_quest():
    quest_name = request.form['quest-name']
    quest_type = request.form['quest-type']
    quest_reward = request.form['quest-reward']

    cursor = db.cursor()
    sql = "INSERT INTO quests (quest_name, quest_type, quest_reward) VALUES (%s, %s, %s)"
    values = (quest_name, quest_type, quest_reward)

    try:
        cursor.execute(sql, values)
        db.commit()
        return "New quest registered successfully."
    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}"
    finally:
        cursor.close()




@app.route('/player-list')
def player_list():
    cursor = db.cursor()
    query = "SELECT * FROM Players"
    cursor.execute(query)
    players = cursor.fetchall()
    cursor.close()
    return render_template('player.html', players=players)
@app.route('/skills-list')
def skills_list():
    cursor = db.cursor()
    query = "SELECT * FROM skills"
    cursor.execute(query)
    skills = cursor.fetchall()
    cursor.close()
    return render_template('Skills.html', skills=skills)

@app.route('/zones-list')
def zones_list():
    cursor = db.cursor()
    query = "SELECT * FROM zones"
    cursor.execute(query)
    zones = cursor.fetchall()
    cursor.close()
    return render_template('Zones.html', zones=zones)

@app.route('/register-item', methods=['POST'])
def register_item():
    item_name = request.form['item_name']
    item_type = request.form['item_type']
    item_rarity = request.form['item_rarity']

    cursor = db.cursor()
    sql = "INSERT INTO item (item_name, item_type, item_rarity) VALUES (%s, %s, %s)"
    values = (item_name, item_type, item_rarity)

    try:
        cursor.execute(sql, values)
        db.commit()
        return "New item registered successfully."
    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}"
    finally:
        cursor.close()





@app.route('/form/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['passwords']
    country = request.form['Country']
    cur = db.cursor()
    cur.execute("INSERT INTO Players (username, email, passwords, country) VALUES (%s, %s, %s, %s)", (username, email, password, country))
    db.commit()
    cur.close()
    return redirect(url_for('registration_successful'))

@app.route('/register-skill', methods=['GET', 'POST'])
def register_skill():
    if request.method == 'POST':
        skill_name = request.form['skill-name']
        skill_type = request.form['skill-type']
        skill_damage = request.form['skill-damage']

        cursor = db.cursor()
        query = "INSERT INTO skills (skill_name, skill_type, skill_damage) VALUES (%s, %s, %s)"
        values = (skill_name, skill_type, skill_damage)
        cursor.execute(query, values)
        db.commit()
        cursor.close()

        return "Skill registered successfully!"

    return render_template('register_skill.html')

@app.route('/register-zone', methods=['GET', 'POST'])
def register_zone():
    if request.method == 'POST':
        zone_name = request.form['zone-name']
        zone_level = request.form['zone-level']
        zone_type = request.form['zone-type']

        cursor = db.cursor()
        query = "INSERT INTO zones (zone_name, zone_level, zone_type) VALUES (%s, %s, %s)"
        values = (zone_name, zone_level, zone_type)
        cursor.execute(query, values)
        db.commit()
        cursor.close()

        return "Zone registered successfully!"

    return render_template('register_zone.html')

@app.route('/registration_successful')
def registration_successful():
    return "Registration success!"


@app.route('/success')
def success():
    return 'Successfully registered!'

@app.route('/overview')
def overview():
    return render_template('Overview.html')

@app.route('/players')
def players():
    return render_template('player.html')

@app.route('/characters')
def characters():
    return render_template('Characters.html')

@app.route('/items')
def items():
    return render_template('Items.html')

@app.route('/quests')
def quests():
    return render_template('Quests.html')

@app.route('/zones')
def zones():
    return render_template('Zones.html')

@app.route('/skills')
def skills():
    return render_template('Skills.html')

@app.route('/diagram')
def diagram():
    return render_template('erd.html')

@app.route('/form/find', methods=['GET'])
def find_player():
    email = request.args.get('player-email')

    # Players 테이블에서 해당 이메일의 플레이어 정보 가져오기
    player = get_player_by_email(email)

    # Characters 테이블에서 해당 이메일을 외래 키로 가지는 캐릭터 정보 가져오기
    characters = get_characters_by_email(email)

    if player:
        # 결과를 화면에 작성하여 출력
        output = f"Player: {player['username']}, Email: {player['email']}\n"
        output += "Characters:\n"
        for character in characters:
            output += f"- {character['character_name']}\n"
        return output
    else:
        return f"Player with email '{email}' not found."

def get_player_by_email(email):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Players WHERE email = %s"
    cursor.execute(query, (email,))
    player = cursor.fetchone()
    cursor.close()
    return player

def get_characters_by_email(email):
    cursor = db.cursor(dictionary=True)
    query = "SELECT character_name FROM Characters WHERE player_email = %s"
    cursor.execute(query, (email,))
    characters = cursor.fetchall()
    cursor.close()
    return characters


@app.route('/form/delete', methods=['POST'])
def delete_player():
    email = request.form['player-email']

    # Characters 테이블에서 해당 이메일을 외래 키로 가지는 캐릭터 정보 삭제
    delete_characters_by_email(email)

    # Players 테이블에서 해당 이메일의 플레이어 정보 삭제
    delete_player_by_email(email)

    return "Player and characters deleted successfully."

def delete_characters_by_email(email):
    cursor = db.cursor()
    query = "DELETE FROM Characters WHERE player_email = %s"
    cursor.execute(query, (email,))
    db.commit()
    cursor.close()

def delete_player_by_email(email):
    cursor = db.cursor()
    query = "DELETE FROM Players WHERE email = %s"
    cursor.execute(query, (email,))
    db.commit()
    cursor.close()

if __name__ == '__main__':
    app.run()
