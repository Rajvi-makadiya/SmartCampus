from flask import render_template

from controllers.team_controllers import team

@team.route('/team-role' , methods=['GET'] , endpoint='team-course')
def team_role():
    return render_template('course/../../templates/role.html')