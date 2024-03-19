from flask import Blueprint, jsonify, request, abort


@Blueprint.route('clothing-recommendations', methods=['GET'])
def get_clothing_recommendation():
    pass