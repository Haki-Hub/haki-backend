from flask import Blueprint, request, jsonify
import logging
from app.services.bill_service import create_full_bill, get_all_bills, get_bill, update_bill, delete_bill
from app.services.part_service import create_part, get_all_parts, get_part, update_part, delete_part
from app.services.section_service import create_section, get_all_sections, get_section, update_section, delete_section
from app.services.chapter_service import create_chapter, get_all_chapters, get_chapter, update_chapter, delete_chapter

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bill Routes
@main.route('/bills/full', methods=['POST'])
def add_bill():
    try:
        data = request.get_json()
        logger.info(f"Received data: {data}")
        if not data:
            return jsonify({"message": "No data provided"}), 400

        bill, status_code = create_full_bill(data)
        return jsonify(bill), status_code
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"message": str(e)}), 400

@main.route('/bills', methods=['GET'])
def get_bills():
    bills = get_all_bills()
    return jsonify(bills)

@main.route('/bills/<int:bill_id>', methods=['GET'])
def get_single_bill(bill_id):
    bill = get_bill(bill_id)
    if bill:
        return jsonify(bill)
    else:
        return jsonify({"message": "Bill not found"}), 404

@main.route('/bills/<int:bill_id>', methods=['PUT'])
def edit_bill(bill_id):
    data = request.get_json()
    bill = update_bill(bill_id, data)
    if bill:
        return jsonify(bill)
    else:
        return jsonify({"message": "Bill not found"}), 404

@main.route('/bills/<int:bill_id>', methods=['DELETE'])
def remove_bill(bill_id):
    bill = delete_bill(bill_id)
    if bill:
        return jsonify({"message": "Bill deleted"})
    else:
        return jsonify({"message": "Bill not found"}), 404

# Part Routes
@main.route('/parts', methods=['POST'])
def add_part():
    data = request.get_json()
    part = create_part(data)
    return jsonify(part), 201

@main.route('/parts', methods=['GET'])
def get_parts():
    parts = get_all_parts()
    return jsonify(parts)

@main.route('/parts/<int:part_id>', methods=['GET'])
def get_single_part(part_id):
    part = get_part(part_id)
    if part:
        return jsonify(part)
    else:
        return jsonify({"message": "Part not found"}), 404

@main.route('/parts/<int:part_id>', methods=['PUT'])
def edit_part(part_id):
    data = request.get_json()
    part = update_part(part_id, data)
    if part:
        return jsonify(part)
    else:
        return jsonify({"message": "Part not found"}), 404

@main.route('/parts/<int:part_id>', methods=['DELETE'])
def remove_part(part_id):
    part = delete_part(part_id)
    if part:
        return jsonify({"message": "Part deleted"})
    else:
        return jsonify({"message": "Part not found"}), 404

# Section Routes
@main.route('/sections', methods=['POST'])
def add_section():
    data = request.get_json()
    section = create_section(data)
    return jsonify(section), 201

@main.route('/sections', methods=['GET'])
def get_sections():
    sections = get_all_sections()
    return jsonify(sections)

@main.route('/sections/<int:section_id>', methods=['GET'])
def get_single_section(section_id):
    section = get_section(section_id)
    if section:
        return jsonify(section)
    else:
        return jsonify({"message": "Section not found"}), 404

@main.route('/sections/<int:section_id>', methods=['PUT'])
def edit_section(section_id):
    data = request.get_json()
    section = update_section(section_id, data)
    if section:
        return jsonify(section)
    else:
        return jsonify({"message": "Section not found"}), 404

@main.route('/sections/<int:section_id>', methods=['DELETE'])
def remove_section(section_id):
    section = delete_section(section_id)
    if section:
        return jsonify({"message": "Section deleted"})
    else:
        return jsonify({"message": "Section not found"}), 404

# Chapter Routes
@main.route('/chapters', methods=['POST'])
def add_chapter():
    data = request.get_json()
    chapter = create_chapter(data)
    return jsonify(chapter), 201

@main.route('/chapters', methods=['GET'])
def get_chapters():
    chapters = get_all_chapters()
    return jsonify(chapters)

@main.route('/chapters/<int:chapter_id>', methods=['GET'])
def get_single_chapter(chapter_id):
    chapter = get_chapter(chapter_id)
    if chapter:
        return jsonify(chapter)
    else:
        return jsonify({"message": "Chapter not found"}), 404

@main.route('/chapters/<int:chapter_id>', methods=['PUT'])
def edit_chapter(chapter_id):
    data = request.get_json()
    chapter = update_chapter(chapter_id, data)
    if chapter:
        return jsonify(chapter)
    else:
        return jsonify({"message": "Chapter not found"}), 404

@main.route('/chapters/<int:chapter_id>', methods=['DELETE'])
def remove_chapter(chapter_id):
    chapter = delete_chapter(chapter_id)
    if chapter:
        return jsonify({"message": "Chapter deleted"})
    else:
        return jsonify({"message": "Chapter not found"}), 404
